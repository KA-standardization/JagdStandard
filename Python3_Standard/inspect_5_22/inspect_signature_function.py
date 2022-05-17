import inspect

import inspect_example

sign = inspect.signature(inspect_example.module_level_function)
print(sign)
print('=' * 88)

for name, param in sign.parameters.items():
    # print('{} : {}'.format(name, param))
    if param.kind == inspect.Parameter.POSITIONAL_ONLY:
        print('  {} (positional only)'.format(name))
    elif param.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD:
        # print('  {} (positional or keyword)'.format(name))
        if param.default != inspect.Parameter.empty:
            print('  {}={!r}'.format(name, param.default))
        else:
            print('   {}'.format(name))
    elif param.kind == inspect.Parameter.VAR_POSITIONAL:
        print('   *{}'.format(name))
    elif param.kind == inspect.Parameter.KEYWORD_ONLY:
        if param.default != inspect.Parameter.empty:
            print('  {}={!r} (keyword-only)'.format(name, param.default))
        else:
            print('  {} (keyword-only)'.format(name))
    elif param.kind == inspect.Parameter.VAR_KEYWORD:
        print('  **{}'.format(name))

print('=' * 88)

bind = sign.bind(
    'this is arg1',
    'this is arg2',
    'this is an extra positional argument',
    extra_name_arg='holle',
)
for name, val in bind.arguments.items():
    print('{} = {!r}'.format(name, val))
print('\nCalling')
print(inspect_example.module_level_function(*bind.args, **bind.kwargs))

print('=' * 88)
bind_partial = sign.bind_partial(
    'this is arg1',
)

for name, val in bind_partial.arguments.items():
    print('{} = {!r}'.format(name, val))

bind_partial.apply_defaults()
for name, val in bind_partial.arguments.items():
    print('{}={!r}'.format(name, val))

print(inspect_example.module_level_function(*bind_partial.args, **bind_partial.kwargs))
