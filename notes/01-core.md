# Split a list into chunks: implementation

## What the example does

The final chunk may be shorter. A positive chunk size is required; a zero size raises ValueError instead of creating an infinite loop.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
{
  "items": [
    1,
    2,
    3,
    4,
    5
  ],
  "size": 2
}
```

Expected result:

```json
[
  [
    1,
    2
  ],
  [
    3,
    4
  ],
  [
    5
  ]
]
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
