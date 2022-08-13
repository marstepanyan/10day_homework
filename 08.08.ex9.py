def num_unique_emails(emails):
    unique_emails = []
    for email in emails:
        local_name = email.split('@')[0]
        domain_name = email.split('@')[1]
        local_name = local_name.split("+")[0]
        local_name = local_name.replace(".", "")
        new_email = ''.join([local_name, "@",  domain_name])
        if new_email not in unique_emails:
            unique_emails.append(new_email)
    # print("unique emails: ", unique_emails)
    return len(unique_emails)


emails_lst = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
print(num_unique_emails(emails_lst))
