variable "location" {
    description = "region donde se creara recursos"
    type        =  string
}

variable "resource_group_name" {
    description = "nombre del grupo del recurso donde se creara el recurso"
    type        =  string
}

variable "suffix" {
    description = "nombre del grupo de databricks donde se creara el recurso administrado por databricks" #no es necesario pero solo como por placer de usar el random_string
    type        =  string
}