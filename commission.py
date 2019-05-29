import sys 

lock, stock, barrel = [int(x) for x in sys.argv[1:]]

LOCK_P   = 45
STOCK_P  = 30
BARREL_P = 25

if lock < 1 or stock < 1 or barrel < 1 or lock > 70 or stock > 80 or barrel > 90:
    print("Out of Range")
else:
    sales = lock * LOCK_P + stock * STOCK_P + barrel * BARREL_P

    if sales <= 1000:
        print("Sales: %.2f Commission: %.2f" % (sales, sales * 0.1))
    elif sales > 1001 and sales < 1800:
        print("Sales: %.2f Commission: %.2f" % (sales, (1000 * 0.1) + (sales - 1000) * 0.15))
    else:
        print("Sales: %.2f Commission: %.2f" % (sales, (1000 * 0.1 + 800 * 0.15) + (sales-1800) * 0.2))
