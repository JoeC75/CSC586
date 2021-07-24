node.routable_control_ip = "true"

# Install and execute a script that is contained in the repository.
node.addService(pg.Execute(shell="sh", command="bash /local/repository/silly.sh"))

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
