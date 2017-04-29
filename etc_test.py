from blockchain import blockexplorer

block = blockexplorer.get_block("00000000000000000035d467f3e31a04bd9814bc0aec04b7e5877530b41b4450")

val = 0

for i in range (1,len(block.transactions)):
	#for j in range(len(block.transactions[i].inputs)):
	#	val += block.transactions[i].inputs[j].value

	for k in range(len(block.transactions[i].outputs)):
		val += block.transactions[i].outputs[k].value

	

print(val)
