这个文档记录了我的python学习过程和练习代码


创建该文档时，我已经基本学习完了《python从入门到实践》，学习了部分python-100天从新手到大师，《流畅的python》一书比较难懂，所以下一步的学习方向有一些不明确。感觉就是基础的已经看过了，进阶的又还看不懂。
因此，我觉得按照python-100天从新手到大师中的编排顺序，从头开始，对基础知识进行查漏补缺，并练习，直到完成100天的学习内容（当然实际用时可能远远超过100天）。
在学习过程中，我会尽可能把每个部分的知识点都写出例程连练习，其中遇到的各种问题的解决方法也会一并记录


1、fork
2、git clone https://github.com/Jason-Zhang9309/golangsdk.git ~/go/src/github.com/huaweicloud/golangsdk
3、git remote add upstream https://github.com/huaweicloud/golangsdk.git
4、git remote -v
5、git fetch upstream
6、git checkout master
7、git merge upstream/master
8、git push origin master
9、git checkout -b  dev
10、写代码
11、git add .
12、git commit -m “注释”
13、git push orgin dev
14、pull request
15、等待代码合并，或修改重新提交（git commit --amend） 
16、git branch -D dev
17、git push origin --delete dev

###每次开发需重复5-17
go get github.com/huaweicloud/golangsdk
go mod vendor

resource "huaweicloud_vpc_v1" "test" {
  name = "zhangjishu-cce-test"
  cidr = "192.168.0.0/16"
}

resource "huaweicloud_vpc_subnet_v1" "test" {
  name          = "zhangjishu-cce-test"
  cidr          = "192.168.0.0/16"
  gateway_ip    = "192.168.0.1"

  //dns is required for cce node installing
  primary_dns   = "100.125.1.250"
  secondary_dns = "100.125.21.250"
  vpc_id        = huaweicloud_vpc_v1.test.id
}


data "huaweicloud_availability_zones" "myaz" {}

resource "huaweicloud_vpc_eip" "myeip" {
  publicip {
    type = "5_bgp"
  }
  bandwidth {
    name        = "zhangjishu-cce-test"
    size        = 8
    share_type  = "PER"
    charge_mode = "traffic"
  }
}

resource "huaweicloud_compute_keypair" "test-keypair" {
  name       = "zhangjishu-keypair"
}
resource "huaweicloud_cce_cluster" "test" {
  name                   = "zhangjishu-cce-test"
  flavor_id              = "cce.s1.small"
  vpc_id                 = huaweicloud_vpc_v1.test.id
  subnet_id              = huaweicloud_vpc_subnet_v1.test.id
  container_network_type = "overlay_l2"
  eip                    = huaweicloud_vpc_eip.myeip.address
}

resource "huaweicloud_cce_node" "node" {
  cluster_id        = huaweicloud_cce_cluster.test.id
  name              = "node"
  flavor_id         = "t6.large.2"
  availability_zone = data.huaweicloud_availability_zones.myaz.names[0]
  key_pair          = huaweicloud_compute_keypair.test-keypair.name

  root_volume {
    size       = 40
    volumetype = "SAS"
  }
  data_volumes {
    size       = 100
    volumetype = "SAS"
  }
}


data "huaweicloud_cce_cluster" "cluster_by_id" {
	id = huaweicloud_cce_cluster.test.id
}

output "found_cluster" {
    value = "${data.huaweicloud_cce_cluster.cluster_by_id.kube_config_raw}"
}



resource "huaweicloud_cce_node_pool" "node_pool" {
cluster_id = huaweicloud_cce_cluster.test.id
name = "testpool"
os = "EulerOS"
initial_node_count = 2
flavor_id = "sn3.large.2"
password = "JDYkS1oydTcxQ0Q0SmpRbmVBeSRXRjVkc29PalRnYzlSRDQ2aTQ2Y0NMM0g5MkxNRW83OHMwckhkZlNMREU4UFc3eWxFMklDY3hVR0Y3LzhSQmJueFcwY3JnQTNaR05GQTBMTGdGYVlEMA=="
scall_enable = true
min_node_count = 1
max_node_count = 10
scale_down_cooldown_time = 100
priority = 1

root_volume {
size = 50
volumetype = "SAS"
}
data_volumes {
size = 100
volumetype = "SAS"
}
}
