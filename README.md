# supSMSGecko
A tool to make Gecko codes for Super Mario Sunshine.

## Installation
```
pip install supSMSGecko
```

You also need [devkitPro](https://github.com/devkitPro/installer/releases) if you want to make C0/C2 codes.

## Example
```python
from supSMSGecko import make_xml, symbols, Button as B

def main(g, ver):
  S = symbols[ver]
  addr_inst = 0x26 + S['TMarDirector_direct']
  addr_input = S['mPadStatus']
  # code
  g.write16(addr_inst, 600)
  g.if16(addr_input, '==', B.B | B.DL)
  g.write16(addr_inst, 2400)
  g.if16(addr_input, '==', B.B | B.DR, endif=True)
  g.write16(addr_inst, 4800)
  g.endif()

# output the generated Gecko codes for all 4 versions to "@code.xml"
make_xml(main)
```

## TODO
- [ ] document of each function
