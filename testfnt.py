from blockchain import blockexplorer
import blocktx_data as b

# test number of total transactions
def test_tot_tx():
    assert(b.tot_tx("000000000000000000b37c165a79af2a4c2663634d233c0bf09d099e54713bb6") == 2757)
    assert(b.tot_tx("000000000000000001e948e8dae3e14d7edea8514bab7c3dfdb298f0e24f5958") == 1423)
    assert(b.tot_tx("000000000000000001d97799bdce61334e0726560f2372bfbf636bf4068f0049") == 1996)
    print("test_tot_tx passed!")
    
def test_avg_tx_val():
    return 0

def test_avg_tx_fee():
    checkval1 = 2.30371195/2757
    assert(abs(b.avg_tx_fee("000000000000000000b37c165a79af2a4c2663634d233c0bf09d099e54713bb6") - checkval1) < 0.0000001)
	checkval2 = 1.07332386/1423
    assert(abs(b.avg_tx_fee("000000000000000001e948e8dae3e14d7edea8514bab7c3dfdb298f0e24f5958") - checkval2) < 0.0000001)
	checkval3 = 1.32353777/1996
	assert(abs(b.avg_tx_fee("000000000000000001d97799bdce61334e0726560f2372bfbf636bf4068f0049") - checkval3) < 0.0000001)
    print("test_avg_tx_fee passed!")
    
def test_avg_tx_size():
    return 0


if __name__ == "__main__":
    test_tot_tx()
    test_avg_tx_fee()
