variable "resource_group_name" {
    description = "nombre del grupo del recurso donde se creara el recurso"
    type        =  string
}

variable "location" {
    description = "region donde se creara el recurso en azure"
    type        =  string
}

variable "suffix" {
    description = "numero random para uso de nombre unico de recurso en azure"
    type        =  string
}