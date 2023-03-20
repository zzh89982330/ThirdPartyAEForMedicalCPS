from TorchCoder import *

sequences = [[1,2,3,4],
             [5,6,7,8],
             [9,10,11,12]]
encoded, decoded, final_loss  = QuickEncode(sequences, embedding_dim=2)