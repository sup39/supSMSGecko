# SPDX-License-Identifier: MIT
# Copyright (c) 2023 sup39

from supGecko import Gecko
import os
import re

VERSIONS = ['GMSJ01', 'GMSE01', 'GMSP01', 'GMSJ0A']
__dirname__ = os.path.dirname(__file__)

def build(main, version):
  g = Gecko(compile_flags={
    'ld_flags': ['-T', f'{__dirname__}/ldscript/{version}.ld'],
  })
  main(g, version)
  return g

def make_xml(
  main, versions=VERSIONS,
  info_xml='info.xml', out_xml='@code.xml',
  indent=4, tag='code', encoding='utf8',
):
  if type(indent) == int: indent = ' '*indent
  with open(out_xml, 'w', encoding=encoding) as fw:
    def write_sources(indent_src):
      for ver in versions:
        print(f'{indent_src}<source version="{ver}">', file=fw)
        print(build(main, ver).dump_txt(indent_src+indent), file=fw)
        print(f'{indent_src}</source>', file=fw)
    if info_xml is not None and os.path.isfile(info_xml):
      found_tag = False
      with open(info_xml, encoding=encoding) as f:
        for line in f:
          m = re.search(r'^(\s*)</(\S+)\s*>', line)
          if m is not None:
            m_tag = m.group(2)
            if m_tag == tag:
              indent_code = m.group(1)
              write_sources(indent_code+indent)
              found_tag = True
          print(line, end='', file=fw)
      if not found_tag:
        raise Exception(f'Tag "{tag}" not found')
    else:
      print(f'<{tag}>', sep='', file=fw)
      write_sources(indent)
      print(f'</{tag}>', sep='', file=fw)
