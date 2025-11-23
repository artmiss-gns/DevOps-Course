provider "local" {

}

resource "local_file" "myresource" {
  filename = "test-file.txt"
  content  = "Hello There!"
}
