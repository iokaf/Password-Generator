# Password-Generator

Implementation of the Chaos-based password generator proposed in [1].
The implementation is to be hosted on streamlit.
The chaotic map is implemented using [2].


## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
streamlit run app.py
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

MIT License

Copyright (c) 2023 Dr. Ioannis Kafetzis

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Disclaimer
This is a research project and is not intended to be used in production.
The authors are not responsible for any damage caused by the use of this software.
The security of the generated passwords for this implementation has not been evaluated.
The implementation results differ from the results in the paper, due to numerical errors.

## References
[1] Kafetzis, I., Moysis, L., Tutueva, A. et al. A 1D coupled hyperbolic tangent
chaotic map with delay and its application to password generation. 
Multimed Tools Appl 82, 9303–9322 (2023). https://doi.org/10.1007/s11042-022-13657-7

[2] chaos-maps: https://pypi.org/project/chaos-maps/