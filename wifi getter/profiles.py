import subprocess


class Cleaner:
    def __init__(self, part_to_drop):
        self._part_to_drop = part_to_drop

    def _clean(self, dirty):
        return dirty.replace(self._part_to_drop, '').replace('\r', '')


class ProfileGetter(Cleaner):
    def __init__(self):
        super().__init__('    All User Profile     : ')

    def extract_profiles(self):
        raw_txt = self._get_raw_profiles_txt().split('\n')
        profiles = []
        for line in raw_txt:
            if self._part_to_drop in line:
                profiles.append(self._clean(line))
        return profiles

    @staticmethod
    def _get_raw_profiles_txt():
        return subprocess.check_output('netsh wlan show profiles').decode('utf-8')


class PasswordGetter(Cleaner):
    def __init__(self, profiles):
        super().__init__('    Key Content            : ')
        self._profiles = profiles

    def get_profiles_passwords(self):
        profiles_keys = []
        for profile in self._profiles:
            profiles_keys.append(
                {
                    'profile': profile,
                    'key': self._get_key(profile)
                }
            )
        return profiles_keys

    def _get_key(self, profile):
        for line in self._raw_text(profile).split('\n'):
            if self._part_to_drop in line:
                return self._clean(line)

    @staticmethod
    def _raw_text(profile):
        try:
            return subprocess.check_output(f'netsh wlan show profile {profile} key=clear').decode('utf-8')
        except:
            return ''








