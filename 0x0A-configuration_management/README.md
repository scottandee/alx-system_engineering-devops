# 0x0A - Configuration Management
Configuration Management is the art of systematically handling changes to a file or system in a way that it maintains integrity over time. Automation is at the heart of configuration management. Some CM tools are Ansible, Puppet etc.

## Benefits of Configuration Management
1. Quick provisioning of new servers
2. Quick recovery from critical events
3. No more Snowflake servers i.e servers that were configured manually and cant be replicated
4. Version control for server environments
5. Replicated Environoments

## What is DevOps?
This is the practice of automating tasks that used to be done manually to save time, reduce impact of human error and increase scalability.

## What is Puppet
Puppet is an open-source configuration management tool that automates deployment and management of IT infrastructure. It makes use of a Declarative language. This language tells us how we want our infrastructure to look like.

## What is a Puppet Resource?
A puppet resource describes something about the state of a system. A group of resources in a file is called a manifest. The syntax for a resource is:
```bash
resource_type { 'resource_name':
      attribute => value
      . . .
}
```

## Some Puppet Basics
1. **Variables**: Varaiables can be used when writing puppet code. It will have to be predeclared before use
   
    ```bash
    $text = "Hello"

    file { '/tmp/test':
            content => $text
            mode    => '0644'
    }
    ```
2. **Loops**: To do this, well have to create a variable which contains an array

    ```bash
    $packages = ['nginx', 'mysql-server']

    package { $packages:
            ensure => installed
    }
    ```
