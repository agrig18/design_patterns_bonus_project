from spore import *


def init_guest_tribe() -> GuestTribe:
    guest_tribe = GuestTribe()

    num_guests = random.randint(1, MAX_MEMBERS)
    for i in range(num_guests):
        energy = random.randint(10, 40)
        guest = Guest(energy=energy,
                      choose_performance=RandomlyChoosePerformance(),
                      apply_features=RandomlyApplyFeatures())
        guest.add_features()
        guest_tribe.add_guest(guest)

    num_instruments = random.randint(1, MAX_INSTRUMENTS)
    for i in range(num_instruments):
        instrument = random.choice(instruments)
        guest_tribe.add_instrument(instrument)

    return guest_tribe


def init_host_tribe() -> HostTribe:
    host_tribe = HostTribe(distribution=RandomlyDistributeCharm())
    num_hosts = random.randint(1, MAX_MEMBERS)

    for i in range(1, num_hosts + 1):
        host_tribe.add_host(Host())

    host_tribe.distribute_composure()

    return host_tribe


if __name__ == "__main__":
    simulation = 0
    while simulation < 100:
        guest_tribe = init_guest_tribe()
        host_tribe = init_host_tribe()

        while True:
            if host_tribe.get_total_composure() <= 0:
                print("Guests have charmed hosts.")
                break
            elif guest_tribe.get_energy() <= 0:
                print("Hosts have disappointed guests.")
                break
            guest_tribe.select_performances()
            guest_tribe.perform()
            tot = guest_tribe.get_total_charm()
            host_tribe.shake_composure(tot)

        simulation += 1
