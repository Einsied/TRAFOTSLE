git push
# publish has to be defined in .ssh/config
ssh publish <<-'ENDSSH'
	./Publish.sh
ENDSSH
