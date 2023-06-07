import smtplib
import requests
for i in range(3):
    # API
    response = requests.get(url="https://api.kanye.rest/")
    data = response.json()
    quote = "Subject: Quote by Kanye West\n\n" + data["quote"]

    #received_email = "spajdrmen555@azet.sk"
    #received_email = "richard.hupka@centrum.sk"
    received_email = "maurykosz@gmail.com"
    my_email = "adamfranko753@gmail.com"
    password = "nxyjghfidbzdzvhs"
    message = "Subject: Imp message\n\nHubla dubla abla permunta"



    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=received_email,
                                msg=quote.encode("utf-8")
                                )