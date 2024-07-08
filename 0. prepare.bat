https://cloud.google.com/vertex-ai/docs/vector-search/quickstart#install-sdk
REM for installation of tensorflow
REM New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force

gcloud init
gcloud config list
gcloud config set project manish-learning
pip install --upgrade "google-cloud-aiplatform>=1.29.0" google-cloud-storage
REM gcloud config set account manish-learning
gcloud auth login manish-learning
gcloud auth application-default login
gcloud auth application-default set-quota-project manish-learning

gcloud services enable compute.googleapis.com aiplatform.googleapis.com storage.googleapis.com --project manish-learning

pip install tensorflow google-cloud-aiplatform tensorflow-hub tensorflow-text 

