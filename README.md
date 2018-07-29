# Gusic
Gusic is web service music recommendation.

# Dependency
- None

# Setup
- Replace foobar with access token.  ( gusic1/hello/views.py )

## How to get access token
1. Visit this page.
https://developer.spotify.com/

2. Log in or Sign up.

3. Create a client ID and client secret.

4. Execute commands below.
If client ID is foo and client secret is bar, Commands are
- $ echo -n foo:bar | base64
	- => hoge

- $ curl -X "POST" -H "Authorization: Basic hoge" -d grant_type=client_credentials https://accounts.spotify.com/api/token
	- => fuga
	- fuga is access token.

# Usage
Clone this repository.

# Licence
None

# Authors
Anvinon
https://anvinon.com/

# Reference
Spotify for Developers
https://developer.spotify.com/