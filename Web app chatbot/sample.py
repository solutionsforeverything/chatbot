import pickle

inputs= pickle.load( open( "vocab2index.p", "rb" ) )

outputs=pickle.load(open("index2vocab.p","rb"))
print("index2vocab")
print(inputs)
print()
print()
print("index2vocab")
print(outputs)