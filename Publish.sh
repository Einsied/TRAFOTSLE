git push
# publish has to ne defined in .ssh/config
ssh publish <<-'ENDSSH'
	./Publish.sh
ENDSSH
