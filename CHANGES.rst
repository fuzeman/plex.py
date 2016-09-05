0.9.0 (2016-09-06)
------------------
**Added**
 - Interfaces
    - :code:`Plex['status'].sessions()`
       - Support for :code:`Photo` sessions
    - :code:`Plex['library'].metadata()`
       - Support for :code:`Photo` metadata objects
 - Methods
    - :code:`Season`
       - :code:`rate(value)`
 - Objects
    - :code:`Photo`
    - :code:`PhotoAlbum`
 - Properties
    - :code:`Clip`
       - :code:`grandparent`
       - :code:`parent`
       - :code:`filename`
       - :code:`device`
    - :code:`Detail`
       - :code:`allow_sharing`
       - :code:`diagnostics`
       - :code:`event_stream`
       - :code:`hub_search`
       - :code:`plugin_host`
       - :code:`read_only_libraries`
       - :code:`updater`
       - :code:`owner_features`
    - :code:`Episode`
       - :code:`absolute_index`
    - :code:`Metadata`
       - :code:`title_sort_saved`
       - :code:`content_rating`
       - :code:`content_rating_age`
       - :code:`rating`
       - :code:`studio`
       - :code:`tagline`
       - :code:`year`
       - :code:`deferred`
       - :code:`created_at_accuracy`
       - :code:`created_at_tzoffset`
       - :code:`deleted_at`
       - :code:`first_scan_added_at`
       - :code:`originally_available_at`
    - :code:`Playlist`
       - :code:`rating_count`
    - :code:`PlaylistItemContainer`
       - :code:`rating_key`
       - :code:`composite`
       - :code:`playlist_type`
    - :code:`Season`
       - :code:`user_rating`
    - :code:`Video`
       - :code:`chapter_images_stale`

**Changed**
 - Improved logging of property parsing errors
 - Properties
    - :code:`Stream`
       - :code:`level` type has been changed to string

**Fixed**
 - Exception would be raised with requests v2.11.0+ when no authentication token has been defined

0.8.0 (2016-02-12)
------------------
**Added**
 - Interfaces
    - :code:`Plex['playlists']`
    - :code:`Plex['playlists/*/items']`
 - Methods
    - :code:`Container`
       - :code:`first()`
    - :code:`Plex['library/metadata']`
       - :code:`update()`
 - Objects
    - :code:`Playlist`
    - :code:`PlaylistItemContainer`
 - Properties
    - :code:`Detail`
       - :code:`allow_media_deletion`
       - :code:`background_processing`
       - :code:`companion_proxy`
    - :code:`Episode`
       - :code:`playlist_item_id`
    - :code:`MediaContainer`
       - :code:`leaf_count_added`
       - :code:`leaf_count_requested`
    - :code:`Metadata`
       - :code:`audience_rating`
       - :code:`audience_rating_image`
       - :code:`rating_count`
       - :code:`rating_image`
       - :code:`source_icon`
       - :code:`url`
    - :code:`Movie`
       - :code:`playlist_item_id`
    - :code:`Stream`
       - :code:`language`
       - :code:`language_code`
    - :code:`Track`
       - :code:`chapter_source`
       - :code:`playlist_item_id`
       - :code:`rating`
       - :code:`user_rating`
       - :code:`year`
    - :code:`TranscoderDetail`
       - :code:`lyrics`
       - :code:`photo`
       - :code:`subtitles`
       - :code:`video_remux_only`

0.7.0 (2015-09-12)
------------------
**Added**
 - Support for client headers (:code:`Configuration.client()`, :code:`Configuration.device()` and :code:`Configuration.platform()`)
 - Support for custom headers (:code:`Configuration.headers()`)
 - Descriptors: :code:`Clip`
 - Interfaces: :code:`Plex[':/plugins/<id>/prefs']`, :code:`Plex[':/timeline']`
 - :code:`Detail` - Properties: :code:`allow_camera_upload`, :code:`allow_channel_access`, :code:`allow_sync`, :code:`certificate`
 - :code:`Track` - Properties: :code:`view_count`
 - :code:`Plex['library']` - Methods: :code:`unscrobble()`

**Changed**
 - Flatten titles in the :code:`SectionContainer.filter()` method

**Fixed**
 - Bug in the :code:`to_iterable()` helper method
 - Boolean properties in the :code:`Detail` descriptor

0.6.4 (2015-02-05)
------------------
**Changed**
 - Implemented some missing properties in :code:`Episode` and :code:`Detail` objects
 - Catch XML parsing errors and display error messages for debugging purposes
 - Use :code:`etree.HTMLParser` (if available)
 - Added missing "artist" object in [/library] :code:`metadata()` map

**Fixed**
 - Catch empty response in [:/prefs] :code:`get()` method
 - Thread synchronization issue with :code:`HttpClient` configuration

0.6.3 (2015-01-04)
------------------
- Added support for authentication tokens
- Added "chapter_source" property to [Video] objects
- Fixed install issue when "requests" isn't installed
- Fixed issue where [ObjectManager] couldn't construct properly

0.6.2 (2014-10-30)
------------------
- Converted LICENSE and README to ReStructuredText

0.6.1 (2014-10-23)
------------------
- Cleaned up all_leaves() and children() response parsing

0.6.0 (2014-10-08)
------------------
- Initial release