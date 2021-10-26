import boto3

def MemberJoingSMS(username, password, firstname, surname, address, postcode, age, group):
    client= boto3.client('sns','eu-west-1')
    client.publish(PhoneNumber='+447758607064',Message='Thank you for choosing Lisburn Racquets Club' + '\n\n' + 'Details:' + '\n' + 'Username: ' + username + '\n' + 'Password: ' + password + '\n' + 'Fullname: ' + firstname + ' ' + surname + '\n' + 'Address: ' + address + '\n' + 'Postcode: ' + postcode + '\n' + 'Age: ' + age + '\n' + 'Group: ' + group)

def ChangingPassword(verificationCode):
    client= boto3.client('sns','eu-west-1')
    client.publish(PhoneNumber='+447758607064',Message=verificationCode)
