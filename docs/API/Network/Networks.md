# Networks

## 网络详情

- 接口定义

方法 | 链接 | 描述
--- | --- | ---
GET | /network/networks/{network_id} | 网络详情

- 请求参数

名称 | 可选 | 区域 | 类型 | 描述
--- | --- | --- | --- | ---
network_id | 必填 | path | string | 网络ID

- 响应结构

```
{
    "network": {
        "admin_state_up": true,
        "auto_increment_id": 13,
        "availability_zone_hints": [],
        "availability_zones": [
            "nova"
        ],
        "cache_updated_at": "2018-07-12T03:12:12",
        "created_at": "2018-07-08T15:39:35",
        "description": "",
        "ext": {},
        "id": "c481a931-7fe6-4ba0-8cbe-133f892ebd8d",
        "ipv4_address_scope": null,
        "ipv6_address_scope": null,
        "is_default": false,
        "mtu": 1400,
        "name": "external_for_testing",
        "port_security_enabled": true,
        "provider:network_type": "flat",
        "provider:physical_network": "provider",
        "provider:segmentation_id": null,
        "region_id": "RegionOne",
        "router:external": true,
        "shared": true,
        "status": "ACTIVE",
        "subnets": [],
        "tags": [],
        "tenant_id": "08c4906ef34e4fa88b89d2cc43163eb4",
        "updated_at": "2018-07-08T15:39:35"
    }
}
```

- 响应参数

名称 | 区域 | 类型 | 描述
--- | --- | --- | ---
network | body | dict | -
id | body | string | -
name | body | string | -
admin_state_up | body | boolean | -
tenant_id | body | string | -
region_id | body | string | -
description | body | string | -
provider:network_type | body | string | -
provider:physical_network | body | string | -
provider:segmentation_id | body | integer | -
router:external | body | boolean | -
shared | body | boolean | -
status | body | string | -
subnets | body | list | -
tags | body | list | -
is_default | body | boolean | -
mtu | body | integer | -
port_security_enabled | body | boolean | -
ipv4_address_scope | body | string | -
ipv6_address_scope | body | string | -
availability_zone_hints | body | list | -
availability_zones | body | list | -
created_at | body | string | UTC ISO8601 format
updated_at | body | string | UTC ISO8601 format
auto_increment_id | body | integer | -
ext | body | dict | -



## 网络列表


- 接口定义

方法 | 链接 | 描述
--- | --- | ---
GET | /network/networks?router:external=True | 外部网络
GET | /network/networks?router:external=False | 私有网络

- 响应结构

```
{
    "networks": [
        {
            "admin_state_up": true,
            "auto_increment_id": 13,
            "availability_zone_hints": [],
            "availability_zones": [
                "nova"
            ],
            "cache_updated_at": "2018-07-12T03:10:41",
            "created_at": "2018-07-08T15:39:35",
            "description": "",
            "ext": {},
            "id": "c481a931-7fe6-4ba0-8cbe-133f892ebd8d",
            "ipv4_address_scope": null,
            "ipv6_address_scope": null,
            "is_default": false,
            "mtu": 1400,
            "name": "external_for_testing",
            "port_security_enabled": true,
            "provider:network_type": "flat",
            "provider:physical_network": "provider",
            "provider:segmentation_id": null,
            "region_id": "RegionOne",
            "router:external": true,
            "shared": true,
            "status": "ACTIVE",
            "subnets": [],
            "tags": [],
            "tenant_id": "08c4906ef34e4fa88b89d2cc43163eb4",
            "updated_at": "2018-07-08T15:39:35"
        }
    ],
    "total_count": 1
}
```

- 响应参数

名称 | 区域 | 类型 | 描述
--- | --- | --- | ---
networks | body | dict | -
total_count | body | integer | -
id | body | string | -
name | body | string | -
admin_state_up | body | boolean | -
tenant_id | body | string | -
region_id | body | string | -
description | body | string | -
provider:network_type | body | string | -
provider:physical_network | body | string | -
provider:segmentation_id | body | integer | -
router:external | body | boolean | -
shared | body | boolean | -
status | body | string | -
subnets | body | list | -
tags | body | list | -
is_default | body | boolean | -
mtu | body | integer | -
port_security_enabled | body | boolean | -
ipv4_address_scope | body | string | -
ipv6_address_scope | body | string | -
availability_zone_hints | body | list | -
availability_zones | body | list | -
created_at | body | string | UTC ISO8601 format
updated_at | body | string | UTC ISO8601 format
auto_increment_id | body | integer | -
ext | body | dict | -


## 创建网络

- 接口定义

方法 | 链接 | 描述
--- | --- | ---
POST | /network/networks | 创建网络

- 请求结构
```
# Flat 模式
{
    "network": {
        "name": "123456",
        "shared": false,
        "provider:network_type": "flat",
        "provider:physical_network": "provider",
        "tenant_id": "1311b3c94917491caa95f376f4a82258"
    }
}

# Vlan 模式
{
    "network": {
        "name": "123456",
        "shared": false,
        "provider:network_type": "vlan",
        "provider:physical_network": "self",
        "provider:segmentation_id": 101,
        "tenant_id": "1311b3c94917491caa95f376f4a82258"
    }
}

# Vxlan 模式
{
    "network": {
        "name": "123456",
        "shared": false,
        "provider:network_type": "vxlan",
        "provider:segmentation_id": 101,
        "tenant_id": "1311b3c94917491caa95f376f4a82258"
    }
}
```

- 请求参数

名称 | 可选 | 区域 | 类型 | 描述
--- | --- | --- | --- | ---
network | 必填 | body | dict | -
name | 必填 | body | string | 网络名称
provider:network_type | 必填 | body | string | 网络类型
provider:physical_network | 必填 | body | string | 物理网络
provider:segmentation_id | 必填 | body | integer | 段ID
shared | 必填 | body | boolean | 共享状态


## 更新网络

- 接口定义

方法 | 链接 | 描述
--- | --- | ---
PUT | /network/networks/{network_id} | 更新网络

- 请求结构
```
# 外部网络
{
    "network": {
        "name": "123456",
        "shared": false,
        "admin_state_up": false
    }
}

# 私有网络
{
    "network": {
        "name": "123456",
        "shared": false
    }
}

```

- 请求参数

名称 | 可选 | 区域 | 类型 | 描述
--- | --- | --- | --- | ---
network_id | 必填 | path | string | 网络ID
network | 必填 | body | dict | -
name | 可选 | body | string | 网络名称
shared | 可选 | body | boolean | 共享状态
admin_state_up | 可选 | body | boolean | 启用状态


## 删除网络

- 接口定义

方法 | 链接 | 描述
--- | --- | ---
DELETE | /network/networks/{network_id} | 删除网络

- 请求参数

名称 | 可选 | 区域 | 类型 | 描述
--- | --- | --- | --- | ---
network_id | 必填 | path | string | 网络ID

- 响应结构

正确结构（204）
```
空
```

错误结构（404）
```
{
    "NeutronError": {
        "detail": "",
        "message": "Network aceb5ba4-3009-40b4-bf08-ea0abde98d71 could not be found.",
        "type": "NetworkNotFound"
    }
}
```
