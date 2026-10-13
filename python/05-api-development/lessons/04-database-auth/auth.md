This usually happens because successful login does not automatically mean Swagger is sending the JWT token to `/auth/me`.

Let's fix it step by step.

## 1. Check the login response

In Swagger, execute `POST /auth/login`. You should receive something like:

```
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}
```

If you get this response, login is working.

## 2. Click the Authorize button

[Simple OAuth2 with Password and Bearer - FastAPI](https://images.openai.com/static-rsc-4/W3ildcP66ZOGT0shtGnaT8qaNKdh6hfE8MsM5fNCtr_SFLjChAapp6E28U-SLw4gH5lpUZ-VqK8_FLxe4sQsknuQ6q89a5L_EbITRrkFTyDsh_xmBVk7hzIfKRfvOhS9f3h7ERJSFXQHrAPQy03KqxGLu8FmKDvSZDhI9XI9wZY?purpose=inline)

Step A — Open Authorize

In the Swagger UI at `http://127.0.0.1:8000/docs`, click the Authorize button near the top of the page.

[OAuth2 with Password (and hashing), Bearer with JWT tokens - FastAPI](https://images.openai.com/static-rsc-4/iu4XVqbBqwhRTBHU01spf-H1IR4CTeiinaXgP38Dj_b1mPaUcPPOROzOTK68oYxh1thrEjuD5jnN8KZK_yPSewRC3PpDRmmKT5US_AX2e9yUrCSkcLuxMf2V02IPBaQSpRn4dHJXzHHQBggn8jeb2FkOONnzCFIyAcwrtBrFZFs?purpose=inline)

Step B — Enter credentials

Enter your registered email in the username field and your password in the password field. Click Authorize, then Close.

Because your code uses `OAuth2PasswordBearer(tokenUrl="/auth/login")`, Swagger can obtain a token through that login endpoint. You generally don't need to copy the token manually.

## 3. Test `/auth/me` again

1. Expand `GET /auth/me`.
2. Click Try it out.
3. Click Execute.

Expected response:

```
{
  "id": 1,
  "email": "dev@example.com"
}
```

## 4. If it still says “Not authenticated”

Check these two things:

- Swagger authorization: After authorizing, make sure the dialog indicates authorization is active. If you only executed `/auth/login`, Swagger might not have stored the token.
- Token header: In the `/auth/me` request's Curl example, verify that it includes a header like:

```
-H 'Authorization: Bearer YOUR_ACCESS_TOKEN'
```

If the header is missing, Swagger is not attaching the token.

One important detail: Your `SECRET_KEY` must remain unchanged while testing. If you restart the terminal and generate a new secret, previously issued tokens become invalid; normally that produces a token-validation error rather than “Not authenticated.”

If it still fails, share the `POST /auth/login` response and the response from `GET /auth/me`. I can pinpoint the issue from those two outputs.