# Contoh String Replace Domain
def replaceDomain(email, oldDomain, newDomain):
    if "@" + oldDomain in email : #? mengecek apakah @oldDomain ada di email
        index = email.index("@" + oldDomain)
        newEmail = email[:index] + "@" + newDomain
        return "this is a new email " + newEmail
    return "this is still a new domain broh : " + email


rightEmail = replaceDomain("thisRight@gmail.com", "yahoo.com", "gmail.com")
wrongEmail = replaceDomain("absolutelyWrong@yahoo.com", "yahoo.com", "gmail.com")
print(rightEmail)
print(wrongEmail)