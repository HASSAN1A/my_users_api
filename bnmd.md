### List of endpoint
- `@user_api.route('/users/range/', defaults = {"start":0, "end": 100} )`
- `@user_api.route('
<int:start>/<int:end>/')`

- `@user_api.route('/users/', defaults = {'n':None})`
- `@user_api.route('/users/<int:n>/')`

- `@user_api.route('/user/<int:val>/')`

- `@user_api.route('/users/<name>/')`

- `@user_api.route('/', methods=['GET'])`

- `@user_api.route('/register', methods = ['GET', 'POST'])`

- `@user_api.route('/login', methods=['POST', 'GET'])`