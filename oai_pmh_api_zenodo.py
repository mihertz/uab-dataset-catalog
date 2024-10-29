from sickle import Sickle
sickle = Sickle('https://zenodo.org/oai2d')
metadataFormats = sickle.ListMetadataFormats()
print(list(metadataFormats))