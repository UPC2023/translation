from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter

# 1. 加载文档
# 我们指定要加载的文件路径
loader = TextLoader("./train_data_2/glossary.txt")
documents = loader.load()

print("--- 原始文档内容 (前500字符) ---")
print(str(documents)[:500])
print("\n" + "="*20 + "\n")


# 2. 分割策略一：按固定字符和分隔符分割 (CharacterTextSplitter)
# 这是一个比较基础的分割器。
# chunk_size: 每个文本块的最大长度。
# chunk_overlap: 文本块之间的重叠字符数，这有助于保持上下文的连续性。
# separator: 用作分割依据的字符，这里我们用换行符。
char_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=100,
    chunk_overlap=20
)
char_split_docs = char_splitter.split_documents(documents)

print("--- 按固定字符分割 (CharacterTextSplitter) 的结果 ---")
print(f"分割后的文档块数量: {len(char_split_docs)}")
print("第一个文档块示例:")
print(char_split_docs[0])
print("\n第二个文档块示例:")
print(char_split_docs[1])
print("\n" + "="*20 + "\n")


# 3. 分割策略二：递归字符分割 (RecursiveCharacterTextSplitter)
# 这是一个更推荐、更智能的分割器。
# 它会尝试按一系列不同的分隔符（如"\n\n", "\n", " ", ""）来分割文本，
# 优先使用能更好地保持语义完整的分割符。
recursive_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)
recursive_split_docs = recursive_splitter.split_documents(documents)

print("--- 按递归字符分割 (RecursiveCharacterTextSplitter) 的结果 ---")
print(f"分割后的文档块数量: {len(recursive_split_docs)}")
print("第一个文档块示例:")
print(recursive_split_docs[0])
print("\n第二个文档块示例:")
print(recursive_split_docs[1])
print("\n" + "="*20 + "\n")

print("观察与思考:")
print("1. 两种分割器产生的文档块数量是否相同？")
print("2. 对比两种分割器产生的第一个块，内容上有什么差异？")
print("3. RecursiveCharacterTextSplitter 尝试优先按段落（双换行符）、然后按句子（换行符）分割，这通常能更好地保留原文的语义结构。")

