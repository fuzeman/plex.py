from plex.objects.core.base import Property, DescriptorMixin


class RateMixin(DescriptorMixin):
    rating = Property(type=float)
    user_rating = Property('userRating', type=float)

    def scrobble(self):
        response = self.request(
            '/:/scrobble',
            query={
                'identifier': 'com.plexapp.plugins.library',
                'key': self.rating_key
            }
        )

        return response.status_code == 200

    def rate(self, value):
        response = self.request(
            '/:/rate',
            query={
                'identifier': 'com.plexapp.plugins.library',
                'key': self.rating_key,
                'rating': int(round(value, 0))
            }
        )

        return response.status_code == 200
