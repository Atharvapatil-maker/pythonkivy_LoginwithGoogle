from kivy.app import App
from kivy.uix.button import Button
from google_auth_oauthlib.flow import InstalledAppFlow

class MyApp(App):
    def build(self):
        self.root = Button(text="Login with Google")
        self.root.bind(on_press=self.login_with_google)
        return self.root

    def login_with_google(self, instance):
        flow = InstalledAppFlow.from_client_secrets_file(
            'jsonfile.json',  # Path to your downloaded client_secret.json file
            scopes=['openid', 'profile', 'email']
        )
        credentials = flow.run_local_server(port=0)
        # You can now use credentials to access Google APIs

if __name__ == '__main__':
    MyApp().run()
