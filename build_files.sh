
echo"BUILD START"
python3 -m pip install -r requirements.txt
python 3 manage.py collectstatic --noinput --clear
echo "BUILD END"
