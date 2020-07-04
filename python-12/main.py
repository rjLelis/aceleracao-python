
doc = '''
#%RAML 1.0
title: Codenation challenge API
mediaType:  application/json
baseUri: http://localhost/codenationchallenge/{version}
version: v1
protocols: [HTTP, HTTPS]
securitySchemes:
  JWT:
    description: JWT based auth.
    type: OAuth 2.0
    describedBy:
      headers:
        Authorization:
          type: string
      responses:
        401:
          description: |
            Invalid or expired Token
    settings:
      signatures : ['HMAC-SHA256']

types:
  Auth:
    type: object
    discriminator: token
    properties: 
        token: string

  Agent:
    type: object
    discriminator: agent_id
    properties: 
      agent_id: integer
      user_id: integer
      name: 
        type: string
        maxLength: 50
      status: boolean
      environment:
        type: string
        maxLength: 20
      version: 
        type: string
        maxLength: 20
      address: 
        type: string
        maxLength: 39
    example:
        agent_id: 5
        user_id: 6
        name: teste
        status: true
        environment: teste
        version: v1
        address: 12.33.55.66

  User:
    type: object
    discriminator: user_id
    properties:
      user_id: integer
      name:
        type: string
        maxLength: 50
      email:
        type: string
        maxLength: 254
      password:
        type: string
        maxLength: 50
      last_login:
        type: date-only
      group_id: integer
        
  Group:
    type: object
    discriminator: group_id
    properties: 
      group_id: integer
      name:
        type: string
        maxLength: 20
    example:
      group_id: 3
      name: teste

  Event:
    type: object
    discriminator: event_id
    properties:
      event_id: integer
      agent_id: integer
      level: 
        type: string
        maxLength: 20
      payload: string
      shelved: boolean
      data: datetime-only
    example:
      event_id: 3
      agent_id: 7
      level: ok
      payload: teste
      shelve: true 
      data: 2020-07-01T07:43:10

/auth/token:
  post:
    description: Create token for a given user
    body:
      application/json:
        username: string
        password: string
    
    responses:
      201:
        body:
          application/json:
            type: Auth
      400:
        body:
          application/json: |
              {"error": "Invalid credencials"}         
      
/agents:
  post:
    description: Adds an agent
    securedBy: JWT
    body:
      application/json:
        properties:
        example: |
          {"user_id": 0,
          "name": "test",
          "status": true,
          "environment": "test",
          "version": "v1",
          "address": "00.00.00.00"
          }
    responses:
      201:
        body:
          application/json:
            example: |
              {"agent_id": 1}
      401:
        body:
          application/json: |
              {"error": "Unauthorized"}
  get:
    description: List agents
    securedBy: JWT
    responses: 
      200:
        body:
          application/json: Agent []
  /{id}:
    get:
      description: Gets an agent by id
      securedBy: JWT
      responses: 
        200:
          body:
            application/json: Agent
        401:
          body:
            application/json: |
              {"error": "Unauthorized"}
        400:
          body:
            application/json: |
              {"error": "Bad Request"}
        404:
          body:
            application/json: |
              {"error": "Not Found"}
    put:
      description: Updates an agent with a given id
      securedBy: JWT
      responses: 
        200:
          body:
            application/json: Agent
        401:
          body:
            application/json: |
              {"error": "Unauthorized"}
        400:
          body:
            application/json: |
              {"error": "Bad Request"}
        404:
          body:
            application/json: |
              {"error": "Not Found"}
    delete:
      description: Deletes and agent with a given id
      securedBy: JWT
      responses:
        204:
          body:
            application/json:
        401:
          body:
            application/json: |
              {"error": "Unauthorized"}
        400:
          body:
            application/json: |
              {"error": "Bad Request"}
        404:
          body:
            application/json: |
              {"error": "Not Found"}
  /{id}/events:
      post:
        description: Adds an event for a given agent
        securedBy: JWT
        body:
          application/json: Event[]
          responses:
          201:
            body:
              application/json: |
                {"message": "Created"}
          401:
            body:
              application/json: |
                {"error": "Unauthorized"}
          400:
            body:
              application/json: |
                {"error": "Bad Request"}
          404:
            body:
              application/json: |
                {"error": "Not Found"}
      get:
        description: Gets an event for a given agent
        securedBy: JWT
        responses:
          200:
            body:
              application/json: Event[]
          401:
            body:
              application/json: |
                {"error": "Unauthorized"}
          400:
            body:
              application/json: |
                {"error": "Bad Request"}
          404:
            body:
              application/json: |
                {"error": "Not Found"}
      put:
        description: Updates an event for a given user
        securedBy: JWT
        body:
          application/json: Event[]
          200:
            body:
              application/json: |
                {"message": "Ok"}
          401:
            body:
              application/json: |
                {"error": "Unauthorized"}
          400:
            body:
              application/json: |
                {"error": "Bad Request"}
          404:
            body:
              application/json: |
                {"error": "Not Found"}
      delete:
        description: Deletes an event for agiven agent
        securedBy: JWT
        body:
          application/json: Event[]
          200:
            body:
              application/json: |
                {"message": "Ok"}
          401:
            body:
              application/json: |
                {"error": "Unauthorized"}
          400:
            body:
              application/json: |
                {"error": "Bad Request"}
          404:
            body:
              application/json: |
                {"error": "Not Found"}    
      /{id}:
        get:
          description: Get a event by id
          securedBy: JWT
          body:
            application/json:
          responses: 
            200:
              body:
                application/json: |
                  {"message": "Ok"}
            401:
              body:
                application/json: |
                  {"error": "Unauthorized"}
            400:
              body:
                application/json: |
                  {"error": "Bad Request"}
            404:
              body:
                application/json: |
                  {"error": "Not Found"} 
        post:
          description: Adds event
          securedBy: JWT
          body:
            application/json:
          responses: 
            200:
              body:
                application/json: |
                  {"message": "Ok"}
            401:
              body:
                application/json: |
                  {"error": "Unauthorized"}
            400:
              body:
                application/json: |
                  {"error": "Bad Request"}
            404:
              body:
                application/json: |
                  {"error": "Not Found"} 
        put:
          description: Updates an event by id
          securedBy: JWT
          body:
            application/json:
          responses: 
            200:
              body:
                application/json: |
                  {"message": "Ok"}
            401:
              body:
                application/json: |
                  {"error": "Unauthorized"}
            400:
              body:
                application/json: |
                  {"error": "Bad Request"}
            404:
              body:
                application/json: |
                  {"error": "Not Found"} 
        delete:
          description: Deletes an event by id
          securedBy: JWT
          body:
            application/json:
          responses: 
            200:
              body:
                application/json: |
                  {"message": "Ok"}
            401:
              body:
                application/json: |
                  {"error": "Unauthorized"}
            400:
              body:
                application/json: |
                  {"error": "Bad Request"}
            404:
              body:
                application/json: |
                  {"error": "Not Found"} 
/groups:
  get:
    description: List groups
    securedBy: JWT
    responses: 
      200:
        body: 
          application/json: Group[]
      401:
        body:
            application/json:
              example: |
                {"error": "Unauthorized"}
  post: 
    description: Adds a group
    securedBy: JWT
    body:
      application/json:
        properties:
          name: 
            type: string
            maxLength: 20
        example: |
          {"name" : "group_name"}
    responses: 
      201: 
        body:
            application/json: |
              {"message": "Ok"}
      401:
        body:
            application/json: |
              {"error": "Unauthorized"}
      400:
        body:
            application/json: |
              {"error": "Bad Request"}
  /{id}:
    get:
      description: Get group by id
      securedBy: JWT
      responses: 
        200:
          body:
            application/json: Group
        401:
          body:
            application/json: |
                {"error": "Unauthorized"}
        404:
          body:
            application/json: |
              {"error": "Bad Request"}
    put:
      description: Updates a group by id
      securedBy: JWT
      responses:
        200:
          body:
            application/json: |
              {"message": "Ok"}
        401:
          body:
            application/json: |
              {"error": "Unauthorized"}
        400:
          body:
            application/json: |
              {"error": "Bad Request"}
        404:
          body:
            application/json: |
              {"error": "Not Found"} 
    delete:
      description: Deletes a group by id
      securedBy: JWT
      responses:
        200:
          body:
            application/json: |
              {"message": "Ok"}
        401:
          body:
            application/json: |
              {"error": "Unauthorized"}
        400:
          body:
            application/json: |
              {"error": "Bad Request"}
        404:
          body:
            application/json: |
              {"error": "Not Found"} 
/users:
  post:
    description: Adds a user
    securedBy: JWT
    body:
      application/json:
        properties:
          name:
            type: string
            maxLength: 50
          password:
            type: string
            maxLength: 50
          email:
            type: string
            maxLength: 254
          last_login:
            type: date-only
        example: |
            {"name": "User",
            "email": "test@test.com",
            "password": "teste123",
            "last_login": "2020-07-01"
            }
    responses:
      201:
        body:
            application/json: |
              {"message": "Ok" }
      401:
        body:
            application/json: |
              {"error": "Unauthorized"}
      401:
        body:
            application/json: |
              {"error": "Unauthorized"}
        400:
          body:
            application/json: |
              {"error": "Bad Request"}
  get:
    description: List users
    securedBy: JWT
    responses:
      200:
        body:
            application/json: User[]
      401:
        body:
            application/json: |
              {"error": "Unauthorized"}

  /{id}:
    get: 
      description: Get user by id
      securedBy: JWT
      responses:
        200:
          body:
            application/json: User
        401:
            body:
              application/json: |
                {"error": "Unauthorized"}
        400:
            body:
              application/json: |
                {"error": "Bad Request"}
        404:
            body:
              application/json: |
                {"error": "Not Found"} 
    put:
      description: Updates an user by id
      securedBy: JWT
      responses:
        200:
          body:
            application/json: |
              {"message": "Ok"}
        401:
          body:
            application/json: |
              {"error": "Unauthorized"}
        400:
          body:
            application/json: |
              {"error": "Bad Request"}
        404:
          body:
            application/json: |
              {"error": "Not Found"} 
    delete:
      description: Deletes an user by id
      securedBy: JWT
      responses:
        200:
          body:
            application/json: |
              {"message": "Ok"}
        401:
          body:
            application/json: |
              {"error": "Unauthorized"}
        400:
          body:
            application/json: |
              {"error": "Bad Request"}
        404:
          body:
            application/json: |
              {"error": "Not Found"} 
'''
