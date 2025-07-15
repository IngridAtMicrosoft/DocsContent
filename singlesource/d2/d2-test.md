---
title: D2 Test
description: Testing the D2 workflow
ms.topic: overview
ms.date: 07/14/2025
---

# D2 Test

D2 diagram rendering tests.

## Test 1
D2 markup is located in a comment so it doesn't render.

<!--
```d2
A -> B: hello
```
-->
<iframe src="d2.svg" width="1280" height="800" scrolling="no"></iframe>

## Test 2

Another D2 diagram in comments:

<!--
```d2
server: Web Server {
  api: API Layer
  db: Database
}
client: Client App
client -> server.api: HTTP Request
server.api -> server.db: Query
```
-->

## Test 3

A more complex example:

<!--
```d2
users: Users {
  shape: person
}
api: API Gateway {
  shape: cloud
}
microservices: {
  auth: Auth Service
  user: User Service
  order: Order Service
}
database: Database {
  shape: cylinder
}

users -> api: Requests
api -> microservices.auth: Authentication
api -> microservices.user: User data
api -> microservices.order: Orders
microservices.auth -> database: Auth data
microservices.user -> database: User data
microservices.order -> database: Order data
```
-->