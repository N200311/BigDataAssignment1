# Create the 'service-result' directory in the current working directory
mkdir -p "C:\Users\user\Desktop\bd-a1\service-result"

# Copy files from the container to the Windows directory
docker cp bd-a1-container:/home/doc-bd-a1/res_dpre.csv "C:\Users\user\Desktop\bd-a1\service-result\"
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-1.txt "C:\Users\user\Desktop\bd-a1\service-result\"
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-2.txt "C:\Users\user\Desktop\bd-a1\service-result\"
docker cp bd-a1-container:/home/doc-bd-a1/eda-in-3.txt "C:\Users\user\Desktop\bd-a1\service-result\"
docker cp bd-a1-container:/home/doc-bd-a1/vis.png "C:\Users\user\Desktop\bd-a1\service-result\"
docker cp bd-a1-container:/home/doc-bd-a1/k.txt "C:\Users\user\Desktop\bd-a1\service-result\"

# Stop the container
docker stop bd-a1-container

echo "Output files copied to 'C:\Users\user\Desktop\bd-a1\service-result\'"
