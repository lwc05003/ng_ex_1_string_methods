import re

encoded = """
   !!junk-77!! | [3::DW::ok] | [xx::DRSC::bad] |
   [1::NFFU::ok] | ##nothing## | [5::TQI_QNGWFWD::ok] |
   [2::OG::ok] | [4::XLI::ok] | [7::WT7::bad] |
   [6::GZ_7_VS::ok] | [99::IGNORE_ME::bad] | %%noise%%
"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 提取所有 [数字::文本::状态] 片段
pattern = r'\[(\d+)::([A-Z0-9_]+)::(ok|bad)\]'
matches = re.findall(pattern, encoded)

# 存储有效片段 (数字, 解码后的文本)
fragments = []

for num_str, jumbled, status in matches:
    if status == 'bad':
        continue
    num = int(num_str)
    decoded_chars = []
    for ch in jumbled:
        if ch in alphabet:
            # 向前移动 num 位（循环）
            idx = alphabet.index(ch)
            new_idx = (idx - num) % 26
            decoded_chars.append(alphabet[new_idx])
        else:
            # 非字母原样保留
            decoded_chars.append(ch)
    decoded_text = ''.join(decoded_chars)
    fragments.append((num, decoded_text))

# 按数字排序并拼接
fragments.sort(key=lambda x: x[0])
final_message = ''.join(text for _, text in fragments)

print(final_message)
