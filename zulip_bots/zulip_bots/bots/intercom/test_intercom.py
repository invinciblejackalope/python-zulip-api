from zulip_bots.test_lib import BotTestCase

class TestHelpBot(BotTestCase):
    bot_name = "intercom"  # type: str

    def test_bot(self) -> None:
        dialog = []

        self.verify_dialog(dialog)
