class RivmDataEntries:
    unix_time = "unix_time"
    aantal_gevallen = "aantal_gevallen"
    laatste_kop = "laatste_kop"

class RivmData(object):
    def __init__(self, unix_time, aantal_gevallen, laatste_kop):
        self.unix_time = unix_time
        self.aantal_gevallen = aantal_gevallen
        self.laatste_kop = laatste_kop
    @classmethod
    def fromDict(cls, input_dict: dict):
        return cls(
            unix_time=input_dict[RivmDataEntries.unix_time],
            aantal_gevallen=input_dict[RivmDataEntries.aantal_gevallen],
            laatste_kop=input_dict[RivmDataEntries.laatste_kop]
        )
    
    def toDict(self):
        return {
            RivmDataEntries.aantal_gevallen: self.aantal_gevallen,
            RivmDataEntries.laatste_kop: self.laatste_kop,
            RivmDataEntries.unix_time: self.unix_time
        }