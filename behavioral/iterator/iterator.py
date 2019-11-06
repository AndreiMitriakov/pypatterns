#!/usr/bin/env python3
# coding: utf-8

from abc import ABC, abstractmethod, ABCMeta


class RadioStation:

    def __init__(self, freq):
        self.freq = freq

    def get_freq(self):
        return self.freq

class StationList:
    def __init__(self):
        self.stations = []
        self.counter = 0

    def add_station(self, station):
        self.stations.append(station)

    def remove_station(self, station_rm):
        freq_rm = station_rm.get_freq()
        self.stations = list(filter(lambda station: station.get_freq() != freq_rm, self.stations))
        
    def count(self):
        return len(self.stations)

    def current(self):
        return self.stations[self.counter]

    def key(self):
        return self.counter

    def next(self):
        self.counter += 1

    def rewind(self):
        self.counter = 0

    def valid(self):
        return self.counter < len(self.stations)

if __name__ == '__main__':
    station_list = StationList()
    station_list.add_station(RadioStation(80))
    station_list.add_station(RadioStation(90))
    station_list.add_station(RadioStation(100))
    station_list.add_station(RadioStation(110))

    for station in station_list.stations:
        print(station.get_freq())

    station_list.remove_station(RadioStation(80))

    for station in station_list.stations:
        print(station.get_freq())



