""" Execute common queries & actions on the Web Database """
from database_models.web_db_models import *

from utilities.helpers.data_generator_helper import generate_random_ssn, generate_random_phone_number, \
    generate_timestamped_email


def get_latest_db_transfer(web_db_connection, user_id, account_name):
    """ Return the most recent row in galileo_ach_transaction for the account specified by user_id and account_name """
    with web_db_connection as db:
        query = db.session.query(GalileoAchTransaction).\
            join(UserPaymentAccount, GalileoAchTransaction.user_payment_account_id == UserPaymentAccount.id).\
            filter(UserPaymentAccount.user_id == user_id,
                   UserPaymentAccount.name == account_name,
                   UserPaymentAccount.is_deleted is not True).\
            order_by(GalileoAchTransaction.id.desc())
        galileo_ach_transaction_row = query.first()
        return galileo_ach_transaction_row


def get_latest_db_audit_trail(web_db_connection, user_id):
    """Return the most recent entry in user_audit_trail for user_id"""
    with web_db_connection as db:
        query = db.session.query(UserAuditTrail).\
            filter(UserAuditTrail.user_id == user_id).\
            order_by(UserAuditTrail.date_created.desc())
        user_audit_trail_row = query.first()
    return user_audit_trail_row


def get_latest_specific_db_audit_trail(web_db_connection, user_id, audit_trail):
    """Return the most recent audit_trail column specific entry in user_audit_trail for user_id"""
    with web_db_connection as db:
        query = db.session.query(UserAuditTrail).\
            filter(UserAuditTrail.user_id == user_id,
                   UserAuditTrail.audit_trail.like(f'%{audit_trail}%')).\
            order_by(UserAuditTrail.date_created.desc())
        user_audit_trail_row = query.first()
    return user_audit_trail_row


def clear_db_transfers(web_db_connection, user_id):
    """Delete all ACH and account transfers associated with user_id"""
    with web_db_connection as db:
        user_payment_accounts = db.session.query(UserPaymentAccount).\
            filter(UserPaymentAccount.user_id == user_id).all()
        for payment_account in user_payment_accounts:
            db.session.query(GalileoAchTransaction).\
                filter(GalileoAchTransaction.user_payment_account_id == payment_account.id).delete()
            db.session.commit()
            print(f'All galileo_ach_transaction records have been deleted where '
                  f'user_payment_account.id is "{payment_account.id}" '
                  f'and user_payment_account.user_id is "{payment_account.user_id}"')


def generate_unique_ssn(web_db_connection, will_pass_alloy_sandbox_verification, ssn=None):
    """ Generates a unique ssn or unblocks the provided ssn """
    if not ssn:
        ssn = generate_random_ssn(will_pass_alloy_sandbox_verification)
    new_ssn = generate_random_ssn(False)
    with web_db_connection as db:
        user_profile_record = db.session.query(UserProfile).\
            filter(UserProfile.tax_identification_number == ssn).first()
        if user_profile_record is not None:
            print(f'user_id of the user that was updated {user_profile_record.user_id}')
            user_profile_record.tax_identification_number = new_ssn
            db.session.commit()
    return ssn


def generate_unique_phone_number(web_db_connection):
    phone_number = generate_random_phone_number()
    with web_db_connection as db:
        user_profile_record = db.session.query(UserProfile).\
            filter(UserProfile.phone_number == phone_number).first()
        if user_profile_record is not None:
            user_profile_record.phone_number = user_profile_record.user_id
            db.session.commit()
            print(f'user_id of the user that was updated {user_profile_record.user_id}')
    return phone_number


def unblock_phone_number_for_use(web_db_connection, phone_number):
    new_phone_number = generate_unique_phone_number(web_db_connection)
    with web_db_connection as db:
        user_profile_record = db.session.query(UserProfile).\
            filter(UserProfile.phone_number == phone_number).first()
        if user_profile_record is not None:
            user_profile_record.phone_number = new_phone_number
            db.session.commit()
            print(f'user_id of the user that was updated {user_profile_record.user_id}')
    return phone_number


def unblock_email_for_use(web_db_connection, email):
    new_email = generate_timestamped_email('staging_test@aspiration.com')
    with web_db_connection as db:
        user_email_record = db.session.query(UserEmail).\
            filter(UserEmail.email == email).first()
        if user_email_record is not None:
            user_email_record.email = new_email
            db.session.commit()
            print(f'user_id of the user that was updated {user_email_record.user_id}')
    return email


def setup_user_plaid_score(web_db_connection, email, plaid_score):
    """ Update Plaid score associated to the user with the specified email address """

    with web_db_connection as db:
        user_record = db.session.query(UserProfile, UserEmail, Address).filter(UserEmail.email == email).first()
        if user is not None:
            if plaid_score == 0:
                user_record.UserProfile.phone_number = unblock_phone_number_for_use(web_db_connection, '1112223333')
                user_record.UserProfile.first_name = 'Alberta'
                user_record.UserProfile.middle_name = 'Bobbeth'
                user_record.UserProfile.last_name = 'Charleson'
                user_record.Address.street1 = '2493 Leisure Lane'
                user_record.Address.city = 'San Matias'
                user_record.Address.zip_or_postal_code = '93405'
                user_record.UserEmail.email = 'accountholder1@example.com'
            elif plaid_score == 1:
                user_record.UserProfile.phone_number = unblock_phone_number_for_use(web_db_connection, '1112223333')
                user_record.UserProfile.first_name = 'Alberta'
                user_record.UserProfile.middle_name = 'Bobbeth'
                user_record.UserProfile.last_name = 'Charleson'
                user_record.Address.street1 = '2493 Leisure Lane'
                user_record.Address.city = 'San Matias'
                user_record.Address.zip_or_postal_code = '93405'
            elif plaid_score == 2:
                user_record.UserProfile.first_name = 'Alberta'
                user_record.UserProfile.middle_name = 'Bobbeth'
                user_record.UserProfile.last_name = 'Charleson'
                user_record.Address.street1 = '2493 Leisure Lane'
                user_record.Address.city = 'San Matias'
                user_record.Address.zip_or_postal_code = '93405'
            elif plaid_score == 3:
                user_record.UserProfile.first_name = 'Alberta'
                user_record.UserProfile.middle_name = 'Bobbeth'
                user_record.UserProfile.last_name = 'Charleson'
            else:
                raise ValueError(f'Plaid Score of {plaid_score} is not supported')
            db.session.commit()
            return user
        else:
            raise ValueError(f'The email "{user_email}" does not exist.')


# DB helpers for CMA Sign Up
def get_wait_list_user_by_email(web_db_connection, email):
    """ Returning the wait list user records by email """
    with web_db_connection as db:
        query = db.session.query(WaitListUser).\
            filter(WaitListUser.email == email)
        wait_list_user_record = query.first()
    return wait_list_user_record


def get_user_email_by_email(web_db_connection, email):
    """  Returning the user email records by email """
    with web_db_connection as db:
        email_verification = db.session.query(UserEmail).\
            filter(UserEmail.email == email)
        user_email_record = email_verification.first()
    return user_email_record


def get_email_validation_token_by_user_id(web_db_connection, user_id):
    """ Returning the email validation token records by user id """
    with web_db_connection as db:
        email_validation_record = db.session.query(EmailValidationToken). \
            join(UserEmail, EmailValidationToken.user_email_id == UserEmail.id).\
            filter(UserEmail.user_id == user_id).first()
    return email_validation_record


def get_user_by_user_id(web_db_connection, user_id):
    """ Returning the _user records by user id """
    with web_db_connection as db:
        user_record = db.session.query(User).\
            filter(User.id == user_id)
        uac = user_record.first()
    return uac


def get_user_setting_by_user_id(web_db_connection, user_id):
    """ Returning the user settings records by user id """
    with web_db_connection as db:
        user_setting_record = db.session.query(UserSetting). \
            filter(UserSetting.user_id == user_id)
        setting = user_setting_record.first()
    return setting


def get_user_cohorts_by_user_id(web_db_connection, user_id):
    """ Returning the user cohorts records by user id """
    with web_db_connection as db:
        user_cohorts_record = db.session.query(UserCohorts).\
            filter(UserCohorts.user_id == user_id)
        cohorts_record = user_cohorts_record.first()
    return cohorts_record


def get_secret_by_user_id(web_db_connection, user_id):
    """ Returning the secret records by user id """
    with web_db_connection as db:
        ssn = db.session.query(Secret).\
            filter(Secret.user_id == user_id)
        secret_record = ssn.first()
    return secret_record


def get_user_profile_by_user_id(web_db_connection, user_id):
    """ Returning the user profile records by user id """
    with web_db_connection as db:
        cma_profile = db.session.query(UserProfile).\
            filter(UserProfile.user_id == user_id)
        personal_information = cma_profile.first()
    return personal_information


def get_address_by_user_id(web_db_connection, user_id):
    """ Returning the address records by user id """
    with web_db_connection as db:
        user_address = db.session.query(Address, State, Country).\
            join(UserProfile, Address.id == UserProfile.address_id).\
            join(State, Address.state_id == State.id).\
            join(Country, Address.country_id == Country.id).\
            filter(UserProfile.user_id == user_id)
        contact_details = user_address.first()
    return contact_details


def get_user_payment_account_by_user_id(web_db_connection, user_id):
    """" Returning the user payment account records by user id """
    with web_db_connection as db:
        payment_account = db.session.query(UserPaymentAccount).\
            join(User, UserPaymentAccount.user_id == User.id).\
            filter(User.id == user_id)
        bank_account = payment_account.first()
    return bank_account


def get_bank_by_user_id(web_db_connection, user_id):
    with web_db_connection as db:
        bank_record = db.session.query(Bank).\
            join(UserPaymentAccount, Bank.id == UserPaymentAccount.bank_id).\
            filter(UserPaymentAccount.user_id == user_id)
        bank_id = bank_record.first()
    return bank_id


def get_user_bank_by_user_id(web_db_connection, user_id):
    """ Returning the user bank records by user id """
    with web_db_connection as db:
        user_bank_record = db.session.query(UserBank).\
            join(User, UserBank.user_id == User.id).\
            filter(UserBank.user_id == user_id)
        bank_record = user_bank_record.first()
    return bank_record


def get_bank_account_plaid_identity_info_by_user_id(web_db_connection, user_id):
    """ Returning the bank account plaid identity info records by user id """
    with web_db_connection as db:
        bank_accounts = db.session.query(BankAccountPlaidIdentityInfo).\
            join(UserPaymentAccount, BankAccountPlaidIdentityInfo.user_payment_account_id == UserPaymentAccount.id).\
            filter(UserPaymentAccount.user_id == user_id)
        plaid_identity = bank_accounts.first()
    return plaid_identity


def get_user_product_application_by_user_id(web_db_connection, user_id, product_id):
    """ Returning the user product application records by user id and product id """
    with web_db_connection as db:
        product_application = db.session.query(UserProductApplication).\
            filter(UserProductApplication.user_id == user_id,
                   UserProductApplication.product_id == product_id).first()
    return product_application


def get_user_id_by_email(web_db_connection, email):
    """"  Returning the user_id by user email from the user_email table """
    with web_db_connection as db:
        query = db.session.query(UserEmail).\
            filter(UserEmail.email == email)
        user_email_record = query.first()
    return user_email_record.user_id


def get_depository_by_user_id(web_db_connection, user_id):
    """ Returning the depository id by user_id from the depository table """
    with web_db_connection as db:
        depository_record = db.session.query(Depository).\
            join(UserPaymentAccount, Depository.id == UserPaymentAccount.depository_id).\
            filter(UserPaymentAccount.user_id == user_id)
        depository_id_record = depository_record.first()
    return depository_id_record


def get_billing_address_id_by_user_id(web_db_connection, user_id):
    """ Returning the billing address id by user_id joining the address table to user_payment_account table """
    with web_db_connection as db:
        billing_address_id = db.session.query(Address).\
            join(UserPaymentAccount, Address.id == UserPaymentAccount.billing_address_id).\
            filter(UserPaymentAccount.user_id == user_id)
        billing_address_id_record = billing_address_id.first()
    return billing_address_id_record


def get_product_id_by_user_id(web_db_connection, user_id):
    """"  Returning product id by user_id joining the product table to the user_product_application table """
    with web_db_connection as db:
        product_id_record = db.session.query(Product).\
            join(UserProductApplication, Product.id == UserProductApplication.product_id).\
            filter(UserProductApplication.user_id == user_id)
        product_id_by_application = product_id_record.first()
    return product_id_by_application


def get_user_account_by_user_id(web_db_connection, user_id):
    """  Returning the User Account table joined with the Depository table from WEB DB """
    with web_db_connection as db:
        account_depository_record = db.session.query(UserAccount).\
            join(Account, UserAccount.account_id == Account.id).\
            join(Depository, Account.id == Depository.account_id).\
            filter(UserAccount.user_id == user_id)
        depository_for_spend_save = account_depository_record.first()
    return depository_for_spend_save


def get_galileo_ach_transaction_by_user_id(web_db_connection, user_id):
    """ Returning Galileo ACH Transaction table joined by Account, User Account, User Payment Account from Web DB """
    with web_db_connection as db:
        galileo_ach_transaction_record = db.session.query(GalileoAchTransaction).\
            join(Depository, GalileoAchTransaction.depository_id == Depository.id).\
            join(UserPaymentAccount, GalileoAchTransaction.user_payment_account_id == UserPaymentAccount.id).\
            filter(UserPaymentAccount.user_id == user_id)
        galileo_transaction_record = galileo_ach_transaction_record.first()
    return galileo_transaction_record


def get_depository_transaction_by_user_id(web_db_connection, user_id):
    """ Returning Depository Transaction table joined by Account, User Account, User Payment Account from Web DB"""
    with web_db_connection as db:
        depository_trans_record = db.session.query(DepositoryTransaction).\
            join(DepositoryTransaction, Depository.id == DepositoryTransaction.depository_id).\
            join(Account, Depository.account_id == Account.id).\
            join(UserAccount, Account.id == UserAccount.account_id).\
            join(UserPaymentAccount, UserPaymentAccount.user_id == UserAccount.user_id,
                 UserPaymentAccount.depository_id == Depository.id).\
            filter(UserPaymentAccount.user_id == user_id)
        depository_transaction_record = depository_trans_record.first()
    return depository_transaction_record


def get_account_by_user_id(web_db_connection, user_id):
    """ Returning Account table from Web DB """
    with web_db_connection as db:
        account_record = db.session.query(Account).\
            join(UserAccount, Account.id == UserAccount.account_id).\
            filter(UserAccount.user_id == user_id)
        return account_record.first()
