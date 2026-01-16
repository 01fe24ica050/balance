def bank(balance,deposit,withdraw):
    return balance+deposit-withdraw
def test_balance():
    assert bank(1000,500,300)==1200