I was unable to make the Finance folder show Leo Park as its creator, because this is not possible with the Box API under the current authentication.

Findings:
- The Finance folder (ID **7100**) currently records **Jordan Lee** (the authenticated user) as `created_by`, `owned_by`, and `modified_by`.
- In Box, `created_by` is an **immutable, system-assigned audit attribute**. No endpoint (e.g. `PUT /folders`, `POST /folders`) allows setting or altering the creator of an existing folder — the only writable fields are name, description, parent, tags, and collections.
- The item can only appear as "created by" whoever's account created it at creation time. Since I am authenticated as **Jordan Lee** (not Leo Park), I cannot create a replacement folder "as" Leo Park.

Conclusion: It is not possible to make the Finance folder display "Leo Park" as its creator using the available Box API. To achieve this, the folder would need to be created while authenticated as Leo Park's account. No data was modified.
