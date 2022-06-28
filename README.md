# EOxServer type-api

A REST API for the type objects of the EOxServer coverages. This allows the modification of `MaskTypes`, `BrowseTypes`, `CoverageTypes`, `ProductTypes`, and `CollectionTypes`.

## Usage

In order to activate the `type-api` configuration has to be added to some files in the Django project:

In `settings.py`:

```python
INSTALLED_APPS = (
    ...

    'rest_framework',
)


```

In `urls.py`:

```python

urlpatterns = [
    ...

    re_path(r'^api/', include("eoxs_type_api.urls")),
]

```

Now the API is mounted under the `api/` endpoint.
