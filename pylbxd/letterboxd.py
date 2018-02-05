from .client import Client


class Letterboxd(object):
    def __init__(self, key, secret):
        self._client = Client(key, secret)

    def _get(self, path, params=None):
        return self._client.request('GET', path, params=params)

    def contributor(self, contributor_id):
        return self._get('contributor/%s' % contributor_id)

    def contributions(self, contributor_id, **params):
        return self._get('contributor/%s/contributions' % contributor_id, params=params)

    def films(self, **params):
        return self._get('films', params=params)

    def film(self, film_id):
        return self._get('film/%s' % film_id)

    def film_availability(self, film_id):
        return self._get('film/%s/availability' % film_id)

    def film_member_relationships(self, film_id, **params):
        return self._get('film/%s/members' % film_id, params=params)

    def film_statistics(self, film_id):
        return self._get('film/%s/statistics' % film_id)

    def lists(self, **params):
        return self._get('lists', params=params)

    def list(self, list_id):
        return self._get('list/%s' % list_id)

    def list_comments(self, list_id, **params):
        return self._get('list/%s/comments' % list_id, params=params)

    def list_entries(self, list_id, **params):
        return self._get('list/%s/entries' % list_id, params=params)

    def list_statistics(self, list_id):
        return self._get('list/%s/statistics' % list_id)

    def log_entries(self, **params):
        return self._get('log-entries', params=params)

    def log_entry(self, log_entry_id):
        return self._get('log-entry/%s' % log_entry_id)

    def log_entry_comments(self, log_entry_id, **params):
        return self._get('log-entry/%s/comments' % log_entry_id, params=params)

    def log_entry_statistics(self, log_entry_id):
        return self._get('log-entry/%s/statistics' % log_entry_id)

    def members(self, **params):
        return self._get('members', params=params)

    def member(self, member_id):
        return self._get('member/%s' % member_id)

    def member_activity(self, member_id, **params):
        return self._get('member/%s/activity' % member_id, params=params)

    def member_list_tags(self, member_id, **params):
        return self._get('member/%s/list-tags-2' % member_id, params=params)

    def member_log_entry_tags(self, member_id, **params):
        return self._get('member/%s/log-entry-tags' % member_id, params=params)

    def member_statistics(self, member_id):
        return self._get('member/%s/statistics' % member_id)

    def member_watchlist(self, member_id, **params):
        return self._get('member/%s/watchlist' % member_id, params=params)

    def search(self, query, **params):
        params.update({'input': query})
        return self._get('search', params=params)
