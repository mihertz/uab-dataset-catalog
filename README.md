# UAB Dataset Catalog

This repository contains the code for the automated API harvesting of dataset records for the AB Dataset Catalog. The catalog is located at https://digitalcommons.library.uab.edu/datasets/. 

Please note that this code is under development and feel free to reach out to Claire at cwarner at rockefeller.edu with any questions, comments, or suggestions. 

## General Workflow

The goal for this project is to search for datasets authored by UAB-affiliated scholars in generalist repositories. Metadata for these datasets is then downloaded as  JSON file. The code then loads in the data as a Pandas dataframe and manipulates it to generate a new dataframe. This dataframe is compatible with the batch upload spreadsheet the corresponds to the collection in the UAB Digital Commons instance where the dataset catalog is hosted.

### De-duplication

To ensure that you are not adding entries that are already in the catalog, you can generate a batch revise spreadsheet showing the current status of the collection. Then, use the notebook titled "remove-existing-dois" to remove any DOIs that are already present in the catalog. 

### Curation and Upload to Digital Commons

After the de-duplicated spreadsheet is output as a .xlsx file you can then manually inspect and enhance the records. You will need to manually re-save it as a .xls file (Pandas does not write to this file type) before proceeding to the batch upload.

## Structure 

The repository is structured in a few sections corresponding to the repositories we access to populate the catalog. Below I have listed the current status of each "section".

### Zenodo

The Zenodo API section is the first one we have completed. It has two functions, allowing you to enter specific DOIs that you would like to process (download via API and reformat to Digital Commons batch upload format) or searching for datasets published within a set timeframe. It will access Zenodo records, as well as some Dryad records which have been mirrored on Zenodo. In the future we will try to develop separate code for Dryad since this mirroring is no longer happening. 

### DataCite

Rather than using a repository-specific API, this code uses the DataCite API to search for datasets that have DOIs minted by DataCite. It accesses Dryad, Zenodo, Figshare, and some other smaller repositories. It then reduces the data (removing multiple DOIs that ccrrespond to the same dataset) and outputs a spreadsheet in the Digital Commons batch upload format. 

 
