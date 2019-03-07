from pypom import Page

from pages.auth0 import Auth0

class Base(Page):
    base_url = "https://web-mozillians.dinopark.infra.iam.mozilla.com/beta/"

    def login(self, email, password, secret_seed):
        auth0 = Auth0(self.base_url)
        auth0.enter_email(email)
        auth0.enter_password(password)
        auth0.enter_passcode(secret_seed)
        #return Homepage(self.driver, self.base_url)
