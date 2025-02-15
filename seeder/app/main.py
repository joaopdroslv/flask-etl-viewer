from generator import generate_product, generate_profile, generate_sale

import time
import random
import os
import sys


if __name__ == '__main__':
    print('[ALERT] Waiting 30 seconds till the MySQL service is up!')
    time.sleep(30)

    for _ in range(100):
        try:
            generate_product()
            print('[PRODUCT] Inserted successfully')
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print("[PRODUCT] [ERROR] ", e, exc_type, fname, exc_tb.tb_lineno)

    for _ in range(50):
        try:
            generate_profile('buyer')
            print('[BUYER] Inserted successfully')
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print("[BUYER] [ERROR] ", e, exc_type, fname, exc_tb.tb_lineno)

    for _ in range(20):
        try:
            generate_profile('seller')
            print('[SELLER] Inserted successfully')
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print("[SELLER] [ERROR] ", e, exc_type, fname, exc_tb.tb_lineno)

    while True:
        try:
            generate_sale()
            print('[SALE] Inserted successfully')
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print("[SALE] [ERROR] ", e, exc_type, fname, exc_tb.tb_lineno)
        finally:
            time.sleep(30)
