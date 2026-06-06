class PaymentError(Exception):
    pass


class InsufficientFundsError(PaymentError):
    pass


class InvalidAmountError(PaymentError):
    pass


def process_payment(amount):
    if not isinstance(amount, (int, float)) or amount < 0:
        raise InvalidAmountError("amount should be a positive number")
    elif amount > 1000:
        raise InsufficientFundsError("not enough funds in account")
    else:
        print(f"Payment of ${amount} processed")


# process_payment('asdas')
# process_payment(-1)
# process_payment(11000)
process_payment(100)
