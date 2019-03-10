# -*- coding: utf-8 -*-
from digitalocean.Record import Record
from digitalocean.baseapi import BaseAPI, GET, POST, DELETE


class Domain(BaseAPI):
    def __init__(self, *args, **kwargs):
        self.name = None
        self.ttl = None
        self.zone_file = None
        self.ip_address = None
        self.id = None

        super(Domain, self).__init__(*args, **kwargs)

    @classmethod
    def get_object(cls, api_token, domain_name):
        """
            Class method that will return a Domain object by ID.
        """
        domain = cls(token=api_token, name=domain_name)
        domain.load()
        return domain

    def load(self):
        # URL https://api.digitalocean.com/v2/domains
        domains = self.get_data("domains/%s" % self.name)
        domain = domains['domain']

        for attr in domain.keys():
            setattr(self, attr, domain[attr])

    def update_domain_record(self, *args, **kwargs):
        """
            Update domain record.
            https://developers.digitalocean.com/#create-a-new-domain-record

            Args:
                type: The record type (A, MX, CNAME, etc).
                name: The host name, alias, or service being defined by the record
                data: Variable data depending on record type.

            Optional Args:
                priority: The priority of the host
                port: The port that the service is accessible on
                weight: The weight of records with the same priority
        """
        data = {
            "type": kwargs.get("type", None),
            "name": kwargs.get("name", None),
            "data": kwargs.get("data", None)
        }

        #  Optional Args
        if kwargs.get("priority", None):
            data['priority'] = kwargs.get("priority", None)

        if kwargs.get("port", None):
            data['port'] = kwargs.get("port", None)

        if kwargs.get("weight", None):
            data['weight'] = kwargs.get("weight", None)

        return self.get_data(
            "domains/%s/records/%s" % (self.name, self.id),
            type=POST,
            params=data
        )
        

    def __str__(self):
        return "%s" % (self.name)