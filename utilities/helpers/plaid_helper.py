def generate_plaid_sandbox_credentials(checking_balance, savings_balance):
    """
        Creates a custom bank account in Plaid sandbox.
        Checkout https://plaid.com/docs/#creating-items-in-the-sandbox for more information.
        This function is only usuable in the Alpha environment.
        Any tests that uses this function must be marked alpha-only.
    """
    plaid_custom_password = {
        "override_accounts":
            [
                {
                    "starting_balance": checking_balance,
                    "type": "depository",
                    "subtype": "checking",
                    "meta": {
                        "name": "Plaid Checking",
                        "number": "1111222233331111"
                    }
                },
                {
                    "starting_balance": savings_balance,
                    "type": "depository",
                    "subtype": "savings",
                    "meta": {
                        "name": "Plaid Saving",
                        "number": "1111222233331111"
                    }
                }
            ]
    }
    return {
        "plaid_username": "user_custom",
        "plaid_password": str(plaid_custom_password)
    }
